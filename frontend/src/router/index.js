import Vue from "vue";
import VueRouter from "vue-router";
import HomePage from "../pages/HomePage.vue";
import LoginPage from "../pages/LoginPage.vue";
import store from "../store";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "homepage",
    component: HomePage,
    meta: { requiresAuth: true }
  },
  {
    path: "/login",
    name: "loginpage",
    component: LoginPage
  },
  {
    path: "*",
    redirect: "/"
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters["auth/isLoggedIn"];
  const token = localStorage.getItem("access");
  //console.log("to.path", to.path);
  // console.log("isLoggedIn=", isLoggedIn);

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (isLoggedIn) {
      // console.log("Already logged in.");
      next();
    } else {
      if (token != null) {
        // console.log("Try reload");
        store
          .dispatch("auth/reload")
          .then(() => {
            // console.log("Successed reloading");
            next();
          })
          .catch(() => {
            forceTorLoginPage(to, from, next);
          });
      } else {
        forceTorLoginPage(to, from, next);
      }
    }
  } else {
    // console.log("GO to public page");
    next();
  }
});

function forceTorLoginPage(to, from, next) {
  next({
    path: "/login",
    query: { next: to.fullPath }
  });
}

export default router;
