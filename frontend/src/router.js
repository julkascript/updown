import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("./views/Home.vue"),
  },
  {
    path: "/songs",
    name: "songs",
    component: () => import("./views/Songs.vue"),
  },
  {
    path: "/songs/:id",
    name: "Song",
    component: () => import("./views/Song.vue"),
  },
  {
    path: "/artists/",
    name: "Artists",
    component: () => import("./views/Artists.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
