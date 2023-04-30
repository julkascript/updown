<!-- views/Home.vue -->
<template>
  <div class="container p-8">
    <div class="p-1 flex flex-col mt-6">
      <h1 class="text-2xl font-bold">Check out the latest translations</h1>
      <div class="grid grid-cols-4 gap-4 mt-12">
        <LatestTranslations />
      </div>
    </div>
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
