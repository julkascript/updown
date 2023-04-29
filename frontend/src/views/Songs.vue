<template>
  <div class="container p-8">
    <h1 class="text-2xl font-bold">Songs</h1>
    <v-table class="mt-10">
      <tbody>
        <tr
          @click="goToSong(song.id)"
          @mouseenter="hover(song)"
          @mouseleave="hover(song)"
          v-for="song in songs"
          :class="{
            'p-4 cursor-pointer': true,
            'bg-slate-200': song.isHovered,
          }"
        >
          <td class="py-4">
            <v-img
              width="5rem"
              aspect-ratio="1/1"
              cover
              class="rounded-lg"
              :src="song.image"
            ></v-img>
          </td>
          <td class="text-2xl">{{ song.artist }}</td>
          <td class="text-2xl">{{ song.title }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script>
import axios from "@/axios";
import { useStore } from "@/store";

export default {
  setup() {
    const store = useStore();

    return {
      getArtistNames: store.getArtistNames,
    };
  },
  data() {
    return {
      songs: [],
    };
  },
  beforeCreate() {
    axios
      .get(`/song/`)
      .then(({ data }) => {
        const formatedData = data.map((song) => {
          const artist = this.getArtistNames(song.artist);
          const { picture_url: image, artist: artistObj, ...rest } = song;
          return {
            artist,
            image,
            isHovered: false,
            ...rest,
          };
        });
        this.songs = formatedData;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    hover(song) {
      song.isHovered = !song.isHovered;
    },
    goToSong(id) {
      this.$router.push(`/songs/${id}`);
    },
  },
};
</script>
