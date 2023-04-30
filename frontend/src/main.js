import { createApp } from "vue";
import { createPinia } from "pinia";
import "./index.css";
import App from "./App.vue";
import router from "@/router";
import "./index.css";
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import axios from "./axios";

axios.interceptors.request.use((config) => {
  // const token = localStorage.getItem('token');
  // if (token) {
  //   config.headers.Authorization = `Bearer ${token}`;
  // }
  config.headers["Content-Type"] = "application/json";
  return config;
});

const vuetify = createVuetify({
  components,
  directives,
});

const pinia = createPinia();

createApp(App).use(router).use(vuetify).use(pinia).mount("#app");
