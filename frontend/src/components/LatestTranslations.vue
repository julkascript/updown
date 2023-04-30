<template>
  <div
    v-for="_ in translations"
    class="container w-100 h-64 shadow-lg rounded-lg bg-slate-100"
  ></div>
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
