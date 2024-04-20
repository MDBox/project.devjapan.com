<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'
import DOMPurify from 'dompurify';
import { marked } from 'marked'
import { baseUrl } from "marked-base-url" 
import Prism from 'prismjs'
import 'prismjs/components/prism-bash'
import 'prismjs/components/prism-javascript'
import 'prismjs/components/prism-python'
import 'prismjs/components/prism-c'
import 'prismjs/components/prism-cpp'
import 'prismjs/components/prism-java'
import 'prismjs/components/prism-go'
import 'prismjs/components/prism-hcl'
import 'prismjs/components/prism-json'
import 'prismjs/components/prism-yaml'
import 'github-markdown-css/github-markdown.css'

defineProps({
  projectPath: {
    type: String,
    required: true
  }
})

const projectPath = ref('raspberry-srt-live-stream')
const projectItem = ref()


marked.use(baseUrl('https://project.devjapan.com/projects/' + projectPath.value ))
marked.setOptions({
  highlight: function(code, lang) {
    if (Prism.languages[lang]) {
      return Prism.highlight(code, Prism.languages[lang], lang);
    } else {
      return code;
    }
  }
});

onMounted(async () => {

  await fetch('https://project.devjapan.com/projects/' + projectPath.value + '/README.md', {
    mode: 'cors'
  })
    .then(response => response.text())
    .then(data => {
      console.log(data)
      console.log(projectItem)
      projectItem.value.innerHTML = DOMPurify.sanitize(marked.parse(data))
      Prism.highlightAll()

    })
    .catch(error => {
      console.error('Error:', error)
    })
})
</script>

<template>
    <section ref="projectItem" class="projectItem">
    </section>
</template>

<style scoped>

.projectItem {
  padding-top: 50px;
  background: var(--color-background);
  max-width: 1024px;
  margin: 0 auto;
  overflow: scroll;
  max-height: 100vh;
}

</style>
