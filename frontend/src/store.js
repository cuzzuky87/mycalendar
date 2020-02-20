import Vue from "vue";
import Vuex from "vuex";
import api from "@/services/api";

Vue.use(Vuex);

const authModule = {
  strict: process.env.NODE_ENV !== "production",
  namespaced: true,
  state: {
    email: "",
    userId: "",
    isLoggedIn: false
  },
  getters: {
    email: state => state.email,
    userId: state => state.userId,
    isLoggedIn: state => state.isLoggedIn
  },
  mutations: {
    set(state, payload) {
      state.email = payload.user.email;
      state.userId = payload.user.id;
      state.isLoggedIn = true;
    },
    clear(state) {
      state.email = "";
      state.isLoggedIn = false;
    }
  },
  actions: {
    /**
     * ログイン
     */
    login(context, payload) {
      return api
        .post("/auth/jwt/create/", {
          email: payload.email,
          password: payload.password
        })
        .then(response => {
          console.log(response);
          localStorage.setItem("access", response.data.access);
          return context.dispatch("reload").then(user => user);
        });
    },
    /**
     * ログアウト
     */
    logout(context) {
      localStorage.removeItem("access");
      context.commit("clear");
    },
    reload(context) {
      return api.get("/auth/users/me/").then(response => {
        const user = response.data;
        context.commit("set", { user: user });
        return user;
      });
    }
  }
};

const messageModule = {
  strict: process.env.NODE_ENV !== "production",
  namespaced: true,
  state: {
    error: "",
    warnings: [],
    info: []
  },
  getters: {
    error: state => state.error,
    warnings: state => state.warnings,
    info: state => state.info
  },
  mutations: {
    set(state, payload) {
      if (payload.error) {
        state.error = payload.error;
      }
      if (payload.warnings) {
        state.warnings = payload.warnings;
      }
      if (payload.info) {
        state.info = payload.info;
      }
    },
    clear(state) {
      state.error = "";
      state.warnings = [];
      state.info = "";
    }
  },
  actions: {
    setErrorMessage(context, payload) {
      context.commit("clear");
      context.commit("set", {
        error: payload.message
      });
    },
    setWarningsMessage(context, payload) {
      context.commit("clear");
      context.commit("set", {
        warnings: payload.message
      });
    },
    setInfoMessage(context, payload) {
      context.commit("clear");
      context.commit("set", {
        info: payload.message
      });
    },
    clearMessages(context) {
      context.commit("clear");
    }
  }
};

const store = new Vuex.Store({
  modules: {
    auth: authModule,
    message: messageModule
  }
});

export default store;
