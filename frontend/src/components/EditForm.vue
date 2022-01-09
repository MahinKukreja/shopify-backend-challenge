<template>
  <div>
    <form required>
      <input
        v-model="id"
        type="number"
        id="id"
        min="0"
        placeholder="Book Number"
      />
      <input v-model="name" type="text" id="name" placeholder="New Book Name" />
      <input
        v-model="author"
        type="text"
        id="author"
        placeholder="New Book Author"
      />
      <input
        v-model="publisher"
        type="text"
        id="publisher"
        placeholder="New Book Publisher"
      />
      <input
        class="submit"
        @click="editBook(id, name, author, publisher)"
        type="button"
        value="Submit"
      />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EditForm",

  methods: {
    editBook(book_id, book_name, book_author, book_publisher) {
      if (
        book_id === null ||
        book_name === null ||
        book_author === null ||
        book_publisher === null
      ) {
        alert("All fields must be filled out");
      } else {
        const new_book = {
          id: book_id,
          name: book_name,
          author: book_author,
          publisher: book_publisher,
        };
        axios.post("http://127.0.0.1:5000/edit_book", new_book).then((res) => {
          alert(res.data);
          this.$root.$emit("new-book-edited", new_book);
        });
      }
    },
  },
};
</script>