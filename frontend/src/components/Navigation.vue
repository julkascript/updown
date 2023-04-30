<template>
  <nav class="top-nav">
    <div class="logo title cursor-pointer">
      <h1 class="text-2xl">
        <router-link to="/">Updown</router-link>
      </h1>
    </div>
    <div class="flex gap-2 mr-auto ml-32">
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
        {
          name: "About",
          path: "/about",
          isActive: false,
        },
      ],
    };
  },
};
</script>

<style scoped>
#about {
  color: black;
  text-decoration: none;
}
button {
  cursor: pointer;
}
.title {
  display: flex;
  align-items: center;
}
.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  background-color: whitesmoke;
  color: black;
}

.logo img {
  height: 2.5rem;
}

.search input {
  border: none;
  padding: 0.5rem;
  margin-right: 0.5rem;
  border-radius: 0.25rem;
}

.search button {
  border: none;
  background-color: #fff;
  color: #333;
  padding: 0.5rem;
  border-radius: 0.25rem;
}

.sign-up button {
  border: none;
  background-color: #fff;
  color: #333;
  padding: 0.5rem;
  border-radius: 0.25rem;
}
</style>
