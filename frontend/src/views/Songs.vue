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
              width="7rem"
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
export default {
  data() {
    return {
      songs: [
        {
          id: 1,
          image:
            "https://i1.sndcdn.com/artworks-iN2l5Lrdfbsxy6Y0-Ia8C7A-t240x240.jpg",
          artist: "Roddy Ricch",
          title: "The Box",
          isHovered: false,
        },
        {
          id: 2,
          image:
            "https://steamuserimages-a.akamaihd.net/ugc/1830164146013510148/26556CEF64B34A3A46A560C7F26D0D92FDE430F9/?imw=512&&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false",
          artist: "Michael Jackson",
          title: "Billie Jean",
          isHovered: false,
        },
        {
          id: 3,
          image:
            "https://i1.sndcdn.com/artworks-9wo2yVLSUwH72KIh-NdBfzQ-t500x500.jpg",
          artist: "Drake",
          title: "More M's",
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
