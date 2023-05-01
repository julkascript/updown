<!-- views/Home.vue -->
<template>
  <div class="px-32 py-16 flex flex-col bg-blue-100">
    <div class="flex">
      <div class="heading p-1 w-full flex flex-col mt-6 gap-4">
        <h1 class="line font-bold text-8xl text-blue-500">Deep dive into</h1>
        <h1 class="line font-bold text-8xl text-blue-700">the ocean of</h1>
        <h1 class="line font-bold text-8xl text-blue-900">lyrics.</h1>
        <button
          class="get-started-btn font-semibold flex justify-center w-1/3 bg-gradient-to-r from-blue-400 to-blue-900 hover:from-sky-500 hover:to-sky-900 text-white mt-10 shadow-md text-l p-3"
        >
          Commence forth
        </button>
      </div>
      <div class="images w-full">
        <img
          src="https://cdn3d.iconscout.com/3d/premium/thumb/translate-6433282-5526034.png"
          alt=""
          class="w-48 h-48 object-contain mx-auto"
        />
        <img
          src="https://cdn3d.iconscout.com/3d/premium/thumb/man-doing-scuba-diving-in-ocean-5597192-4678676.png"
          alt="a"
          class="ml-auto"
        />
      </div>
    </div>
  </div>
  <img class="w-full rotate-180" src="@/assets/wave-blue.png" alt="" />
</template>

<script>
export default {
  components: {},
};
</script>

<style scoped>
.heading,
.line {
  font-family: "Epilogue" !important;
}
.get-started-btn {
  border-radius: 10px 100px / 120px;
}
</style>
