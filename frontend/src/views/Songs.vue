<template>
  <div class="container p-4">
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
              width="7rem"
              aspect-ratio="1/1"
              cover
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
export default {
  data() {
    return {
      songs: [
        {
          id: 1,
          image: "https://cdn.vuetifyjs.com/images/parallax/material.jpg",
          artist: "Roddy Rich",
          title: "The box",
          isHovered: false,
        },
        {
          id: 2,
          image: "https://picsum.photos/200",
          artist: "Michael Jackson",
          title: "Billie Jean",
          isHovered: false,
        },
      ],
    };
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
