document.getElementById('enterrr').addEventListener('click', function() {
  // Get the input values
  const titleValue = document.getElementById('title').value;
  const descriptionValue = document.getElementById('description').value;

  // Create new todo container
  const newTodo = document.createElement('div');
  newTodo.classList.add('todos');

  // Create the title element
  const newTitle = document.createElement('h2');
  newTitle.innerText = titleValue;
  newTodo.appendChild(newTitle);

  // Create the description element
  const newDescription = document.createElement('p');
  newDescription.innerText = descriptionValue;
  newTodo.appendChild(newDescription);

  // Create the delete button
  const deleteButton = document.createElement('button');
  deleteButton.classList.add('delete_btn');
  deleteButton.innerText = 'del';
  newTodo.appendChild(deleteButton);

  // Add delete functionality
  deleteButton.addEventListener('click', function() {
      newTodo.remove();
  });

  // Append the new todo to the container
  document.getElementById('container').appendChild(newTodo);

  // Clear the input fields
  document.getElementById('title').value = '';
  document.getElementById('description').value = '';
});
