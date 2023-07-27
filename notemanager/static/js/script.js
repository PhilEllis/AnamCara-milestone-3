// Delete Note Button - code referenced in README.md
var deleteNoteBtn = document.getElementById("deleteNoteBtn");
deleteNoteBtn.addEventListener("click", function() {
  var noteId = document.getElementById("deleteModal").getAttribute("data-noteid");
  var deleteUrl = "{{ url_for('delete_note', note_id='') }}" + noteId;
  window.location.href = deleteUrl;
});