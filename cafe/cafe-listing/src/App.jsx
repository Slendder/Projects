import './App.css'
import axios from "axios";
import {useState, useEffect} from "react";
import Card from "./components/product.jsx"
function App() {
    const [products, setProducts] = useState([]);
    const [showAll, setShowAll] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            const response = await axios.get("https://raw.githubusercontent.com/devchallenges-io/web-project-ideas/main/front-end-projects/data/simple-coffee-listing-data.json");
            setProducts(response.data);
        }
        fetchData();
    }, []);

    const cardsToShow = () => showAll
        ? products
        : products.filter((product) => product.available === true)

    return (
      <>
        <h1>Our Collection</h1>
        <p className={"paragraph"}>Introducing our Coffee Collection, a selection of unique coffees from different roast types and origins,
          expertly roasted in small batches and shipped fresh weekly.</p>

        <div>
          <section className="buttons">
            <button onClick={() => setShowAll(!showAll)}>
                {showAll ? "Available now" : "All Products"}
            </button>
          </section>
          <div className="products">
              {cardsToShow().map((product) => <Card key={product.id} product={product}/>)}
          </div>
        </div>
      </>
  )
}

export default App
