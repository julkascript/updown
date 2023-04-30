<template>
  <div class="container p-8">
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
          <td class="picture p-4 m-0 align-top w-1/12">
            <v-img
              aspect-ratio="1/1"
              cover
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
