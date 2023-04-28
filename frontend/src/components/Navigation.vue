<template>
  <nav class="top-nav">
    <div class="logo title cursor-pointer">
      <h1 class="text-2xl">
        <router-link to="/">Updown</router-link>
      </h1>
    </div>
    <div class="flex gap-2 mr-auto ml-32">
      <div class="nav-links">
        <router-link to="/translations" id="about">Translations</router-link>
      </div>
      <div class="nav-links">
        <router-link to="/about" id="about">About</router-link>
      </div>
    </div>
    <div class="search">
      <input type="text" placeholder="Search" />
      <button>Search</button>
    </div>
    <!-- <div class="sign-up">
      <button>Sign Up</button>
    </div> -->
  </nav>
</template>

<script>
export default {
  name: "TopBar",
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

.nav-links {
  display: flex;
  color: black;
}

.nav-links a {
  margin-right: 1rem;
  color: #fff;
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
