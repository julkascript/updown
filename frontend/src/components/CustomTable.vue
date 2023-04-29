<template>
  <v-table class="mt-10">
    <tbody>
      <tr
        @click="goToItem(item.id)"
        @mouseenter="hover(item)"
        @mouseleave="hover(item)"
        v-for="item in items"
        :class="{
          'p-4 cursor-pointer': true,
          'bg-slate-200': item.isHovered,
        }"
      >
        <td class="py-4">
          <v-img
            width="5rem"
            aspect-ratio="1/1"
            cover
            class="rounded-lg"
            :src="item.image"
          ></v-img>
        </td>
        <td class="text-2xl">{{ item.name }}</td>
        <!-- <td class="text-2xl">{{ item.title }}</td> -->
      </tr>
    </tbody>
  </v-table>
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
  },
};
</script>
