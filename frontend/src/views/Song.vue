<template>
  <div class="px-32 py-12 flex flex-column gap-12">
    <div class="flex gap-8">
      <img :src="songData.image" class="rounded-lg photo" />
      <div>
        <div class="font-bold title flex flex-row justify-start gap-4 text-4xl">
          <h1 class="text-sky-900">
            {{ songData.title }}
          </h1>
          <h1 class="text-sky-900">/</h1>
          <h1 class="text-sky-900">{{ songData.translatedTitle }}</h1>
        </div>
        <div class="flex flex-row text-xl gap-2 mt-2">
          <h3 class="">{{ songData.artist }}</h3>
          <h3>/</h3>
          <h3>{{ songData.artistTranslated }}</h3>
        </div>
      </div>
    </div>
    <div class="flex flex columns-2 gap-64">
      <div>
        <h3 class="text-2xl font-bold mb-4">Original lyrics / Оригинал</h3>
        <div v-for="paragraph in songData.paragraphs" class="mb-24">
          <h5>[ {{ paragraph.name }} ]</h5>
          <p v-for="line in paragraph.lines">{{ line.content }}</p>
        </div>
      </div>
      <div class="ml-20">
        <h3 class="text-2xl font-bold mb-4">Translated lyrics / Превод</h3>
        <!-- <div
          v-for="lyric in Object.entries(songData.translatedLyrics)"
          class="mb-24"
        >
          <h5>[ {{ lyric[0] }} ]</h5>
          <p>{{ lyric[1] }}</p>
        </div> -->
      </div>
    </div>
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
      getTranslatedArtistNames: store.getTranslatedArtistNames,
    };
  },
  data() {
    return {
      songData: {
        id: undefined,
        image: undefined,
        artist: "",
        title: "",
        lyrics: ``,
        translatedTitle: "",
        translatedLyrics: ``,
      },
    };
  },
  beforeCreate() {
    const id = this.$route.params.id;
    axios
      .get(`/song/${id}/`)
      .then(({ data }) => {
        const artist = this.getArtistNames(data.artist);
        const artistTranslated = this.getTranslatedArtistNames(data.artist);
        const {
          artist: artistObj,
          artistTranslated: artistTranslatedObj,
          translated_title: translatedTitle,
          // translated_lyrics: translatedLyrics,
          picture_url: image,
          ...songDataRest
        } = data;
        this.songData = {
          artist,
          artistTranslated,
          image,
          translatedTitle,
          // translatedLyrics,
          ...songDataRest,
        };
        console.log(this.songData)
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
