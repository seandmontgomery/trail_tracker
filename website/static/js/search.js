const searchBar = document.getElementById('searchBar');
const text = document.getElementsByClassName("card");

function searchCards(queryString) {
  console.log(Object.values(text).filter((t) => !t.outerText.toLowerCase().includes(queryString)))
  console.log(Object.values(text).map((t) => console.log(t.outerText.toLowerCase())))
  return Object.values(text).filter((t) => !t.innerText.toLowerCase().includes(queryString))
}

searchBar.addEventListener('keyup', (evt) => {
  const searchString = evt.target.value;
  let searchResults = searchCards(searchString.toLowerCase())
  for (let i = 0; i < text.length; i++) {
    searchResults.includes(text[i]) ? text[i].style.display = "none" : text[i].style.display = "block"
  }
});
