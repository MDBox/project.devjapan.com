<script setup>
import { RouterLink } from 'vue-router'
import { useRouter } from 'vue-router'

const router = useRouter()

const openProject = (projectPath) => {
  console.log(projectPath)
  router.push({
    name: 'project',
    params: { projectPath }
  })
}
</script>

<template>
  <ul class="list-group">
    <li class="list-group-item" @click="openProject('raspberry-srt-live-stream')">
      <div class="card">
        <div class="card-header">IoT</div>
        <div class="card-body">
          <h5 class="card-title">raspberry-srt-live-stream</h5>
          <p class="card-text"></p>
        </div>
      </div>
    </li>
  </ul>
</template>

<style></style>
