<template>
  <div class="home">
    <MyCalendar />
  </div>
</template>

<script>
import MyCalendar from "../components/MyCalendar";

export default {
  name: "HomePage",
  components: {
    MyCalendar
  },
  data: () => ({})
};
</script>
