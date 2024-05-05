<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'

const props = defineProps({
  projectPath: {
    type: String,
    required: true
  }
})

const projectItem = ref()

onMounted(async () => {
})

</script>

<template>
    <iframe ref="projectItem" class="projectItem" :src="`/projects/${projectPath}`"></iframe>
</template>

<style scoped>

.projectItem {
  padding-top: 50px;
  background: var(--color-background);
  max-width: 100%;
  margin: 0 auto;
  overflow: scroll;
  max-height: 100vh;
}

</style>
