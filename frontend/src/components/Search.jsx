import React from "react";

function Search(props) {
  const [query, setQuery] = React.useState("");

  function handleSubmit(e) {
    e.preventDefault();
    props.submit(query);
    setQuery("");
  }

  return (
    <form action="" className="search-bar" onSubmit={handleSubmit}>
      <input
        type="search"
        name="search"
        pattern=".*\S.*"
        onChange={(e) => setQuery(e.target.value)}
        value={query}
        required
      />
      <button className="search-btn" type="submit">
        <span>Search</span>
      </button>
    </form>
  );
}

export default Search;
