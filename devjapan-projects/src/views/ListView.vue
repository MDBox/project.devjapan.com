<script setup>
import { useRouter } from 'vue-router'
import { onMounted, ref } from 'vue';

const projects = ref([])

const router = useRouter()

const openProject = (projectPath) => {
  console.log(projectPath)
  router.push({
    name: 'project',
    params: { projectPath }
  })
}

onMounted(async () => {
  console.log('ListView mounted')
  const response = await fetch('https://project.devjapan.com/projects.json', {
    mode: 'cors'
  })
  projects.value = await response.json()
  print(projects.value)
})

</script>

<template>
  <ul class="list-group">
    <li class="list-group-item" @click="openProject(project.path)" v-for="project of projects">
      <div class="card">
        <!-- <div class="card-header">IoT</div> -->
        <div class="card-body">
          <h5 class="card-title">{{ project.name }}</h5>
          <p class="card-text"></p>
        </div>
      </div>
    </li>
  </ul>
</template>

<style></style>
