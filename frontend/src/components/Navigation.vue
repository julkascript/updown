<template>
  <nav
    class="flex align-center justify-between top-nav px-32 py-4 border-b-2 border-zinc-gray-950 sticky top-0 bg-white z-50"
  >
    <div class="logo title cursor-pointer">
      <h1 class="text-2xl font-bold text-sky-900">
        <router-link to="/">Updown</router-link>
      </h1>
    </div>
    <div class="flex gap-2 mr-auto ml-32 text-sky-900">
      <div
        v-for="tab in tabs"
        :class="{
          'mr-4': true,
          'font-bold': tab.name?.toLowerCase() === getActiveTab,
        }"
      >
        <router-link :to="tab.path">{{ tab.name }}</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "TopBar",
  computed: {
    getActiveTab() {
      return this.$route?.name?.toLowerCase();
    },
  },
  data() {
    return {
      tabs: [
        {
          name: "Songs",
          path: "/songs",
          isActive: false,
        },
        {
          name: "Artists",
          path: "/artists",
          isActive: false,
        },
      ],
    };
  },
};
</script>
