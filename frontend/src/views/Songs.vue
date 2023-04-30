<template>
  <CustomTable title="Songs" :items="songs" :goTo="goToSong"></CustomTable>
</template>

<script>
import axios from "@/axios";
import { useStore } from "@/store";
import CustomTable from "@/components/CustomTable.vue";

export default {
  name: "Songs",
  components: {
    CustomTable,
  },
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
          const name = this.getArtistNames(song.artist);
          const { picture_url: image, name: artistObj, ...rest } = song;
          return {
            name,
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
