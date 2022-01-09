<template>
  <div>
    <download-csv :data="books_info">
      <button class="dl">Download</button>
    </download-csv>
  </div>
</template>

<script>
export default {
  name: "ToCSV",
  props: {
    books: {
      type: Array,
    },
  },
  data() {
    return {
      books_info: this.books,
    };
  },
};
</script>

<style>
.dl {
  background-color: darkturquoise;
}
</style>