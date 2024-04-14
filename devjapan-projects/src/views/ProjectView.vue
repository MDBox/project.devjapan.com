<script setup>
import TheWelcome from '../components/TheWelcome.vue'
import ProjectItem from '../components/ProjectItem.vue'

defineProps({
  projectPath: {
    type: String,
    required: true
  }
})
</script>

<template>
  <main>
    <ProjectItem :project-path="projectPath" />
  </main>
</template>

<style scoped>
main {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8f9fa;
}
</style>
