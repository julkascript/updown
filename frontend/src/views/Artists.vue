<template>
  <CustomTable
    title="Artists"
    :items="artists"
    :goTo="goToArtist"
  ></CustomTable>
</template>

<script>
import CustomTable from "@/components/CustomTable.vue";
import axios from "@/axios";

export default {
  name: "Artists",
  data() {
    return {
      artists: [],
    };
  },
  components: {
    CustomTable,
  },
  beforeCreate() {
    axios
      .get(`/artist/`)
      .then(({ data }) => {
        console.log(data);
        const formatedData = data.map((artist) => {
          const { picture_url: image, ...rest } = artist;
          return {
            image,
            isHovered: false,
            ...rest,
          };
        });
        this.artists = formatedData;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    goToArtist(id) {
      this.$router.push(`/artists/${id}`);
    },
  },
};
</script>
