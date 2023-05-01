<template>
  <div class="container px-32 py-12">
    <h1 class="text-2xl font-bold">{{ pageTitle }}</h1>
    <table class="mt-10 w-full">
      <tbody>
        <tr
          @click="goTo(item.id)"
          @mouseenter="hover(item)"
          @mouseleave="hover(item)"
          v-for="item in items"
          :class="{
            'p-4 cursor-pointer': true,
            'bg-slate-200': item.isHovered,
            'border-b-2 border-zinc-200': true,
          }"
        >
          <td class="p-4 m-0 align-top">
            <v-img
              cover
              max-height="100"
              max-width="100"
              class="rounded-lg shadow-md"
              :src="item.image"
            ></v-img>
          </td>
          <td class="text-2xl pl-12">{{ item.name }}</td>
          <td v-show="item.title" class="text-2xl pl-12">{{ item.title }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "CustomTable",
  props: {
    items: {
      type: Array,
      required: true,
    },
    goTo: {
      type: Function,
      required: true,
    },
    pageTitle: {
      type: String,
      required: true,
    },
    extraItem: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      headers: {
        align: "left",
        value: "name",
        // sortable: false,
      },
    };
  },
  methods: {
    hover(song) {
      song.isHovered = !song.isHovered;
    },
  },
};
</script>
