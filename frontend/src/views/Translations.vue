<template>
  <div class="container p-4">
    <h1 class="text-2xl font-bold">Translations</h1>
    <v-table class="mt-10">
      <tbody>
        <tr
          @mouseenter="hover(translation)"
          @mouseleave="hover(translation)"
          v-for="translation in translations"
          :class="{
            'p-4 cursor-pointer': true,
            'bg-slate-200': translation.isHovered,
          }"
        >
          <td class="py-4">
            <v-img width="7rem" :src="translation.image"></v-img>
          </td>
          <td class="text-2xl">{{ translation.artist }}</td>
          <td class="text-2xl">{{ translation.title }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      translations: [
        {
          image: "https://cdn.vuetifyjs.com/images/parallax/material.jpg",
          artist: "Roddy Rich",
          title: "The box",
          isHovered: false,
        },
        {
          image: "https://picsum.photos/200",
          artist: "Michael Jackson",
          title: "Billie Jean",
          isHovered: false,
        },
      ],
    };
  },
  methods: {
    hover(translation) {
      translation.isHovered = !translation.isHovered;
    },
  },
};
</script>
