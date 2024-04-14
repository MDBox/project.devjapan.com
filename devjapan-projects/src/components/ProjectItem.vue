<script setup>
defineProps({
  projectPath: {
    type: String,
    required: true
  }
})
</script>

<template>
  <iframe
    :src="'https://project.devjapan.com/projects/' + projectPath"
    width="100%"
    height="100%"
  ></iframe>
</template>

<style scoped></style>
