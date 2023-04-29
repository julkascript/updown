<template>
  <div class="p-8 flex flex-column gap-12">
    <div class="flex gap-8">
      <img :src="songData.image" class="rounded-lg photo" />
      <div>
        <div class="font-bold title flex flex-row justify-start gap-4 text-4xl">
          <h1 class="text-sky-900">
            {{ songData.title }}
          </h1>
          <h1 class="text-sky-900">/</h1>
          <h1 class="text-sky-900">Богато стягане</h1>
        </div>
        <div class="flex flex-row text-xl gap-2 mt-2">
          <h3 class="">{{ songData.artist }}</h3>
          <h3>/</h3>
          <h3>Дракон</h3>
        </div>
      </div>
    </div>
    <div class="flex flex columns-2 gap-64">
      <div>
        <h3 class="text-2xl font-bold mb-4">Original lyrics</h3>
        <div v-for="lyric in Object.entries(songData.lyrics)" class="mb-24">
          <h5>[ {{ lyric[0] }} ]</h5>
          <p>{{ lyric[1] }}</p>
        </div>
      </div>
      <div class="ml-20">
        <h3 class="text-2xl font-bold mb-4">Translated lyrics</h3>
        <div v-for="lyric in Object.entries(songData.lyrics)" class="mb-24">
          <h5>[ {{ lyric[0] }} ]</h5>
          <p>{{ lyric[1] }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "@/axios";

export default {
  data() {
    return {
      songData: {
        id: undefined,
        image: undefined,
        artist: "",
        title: "",
        lyrics: ``,
      },
    };
  },
  beforeCreate() {
    axios
      .get(`/song/1/`)
      .then(({ data }) => {
        const {
          artist: [{ name: artist } = { name: "" }],
          picture_url: image,
          ...songDataRest
        } = data;
        this.songData = { artist, image, ...songDataRest };
        console.log(this.songData.image);
      })
      .catch((err) => console.log(err));
  },
};
</script>

<style>
.photo {
  width: 300px !important;
  height: 300px !important;
  object-fit: cover;
  display: flex;
}
</style>
