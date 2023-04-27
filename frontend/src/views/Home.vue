<!-- views/Home.vue -->
<template>
  <div class="p-1 flex flex-col items-center justify-center mt-6">
    <h1 class="text-2xl font-bold">Check out the latest translations</h1>
    <TranslationList />
  </div>
</template>

<script>
import TranslationList from '../components/TranslationList.vue'
export default {
  components: {
    TranslationList
  }
}
</script>

<style>
</style>