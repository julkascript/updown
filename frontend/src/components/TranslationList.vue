<template>
  <div class="container flex flex-row gap-6 justify-center mt-12">
    <div
      v-for="t in translations"
      class="container bg-zinc-200 w-1/6 h-64"
    ></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      translations: ["a", "b", "c", "d", "e", "f"],
    };
  },
};
</script>
