<script setup>
import { useToastStore } from '@/stores/toast'
const store = useToastStore()
</script>

<template>
  <div
    v-if="store.isVisible"
    class="transition ease-in-out delay-500 duration-500 px-6 py-6 fixed bottom-[30px] rounded-xl shadow-xl mx-auto left-0 right-0 w-fit"
    :class="store.classes"
  >
    {{ store.message }}
  </div>
</template>
