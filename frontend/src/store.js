import { defineStore } from "pinia";

export const useStore = defineStore({
  id: "mainStore",
  state: () => ({}),
  actions: {
    getArtistNames(artists) {
      return artists.map((artist) => artist.name).join(", ");
    },
    getTranslatedArtistNames(artists) {
      return artists.map((artist) => artist.translated_name).join(", ");
    },
  },
});
