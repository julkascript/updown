<!-- views/Home.vue -->
<template>
  <div class="p-1 flex flex-col items-center justify-center mt-6">
    <h1 class="text-2xl font-bold">Check out the latest translations</h1>
    <LatestTranslations />
  </div>
</template>

<script>
import LatestTranslations from "../components/LatestTranslations.vue";
export default {
  components: {
    LatestTranslations,
  },
};
</script>

<style></style>
