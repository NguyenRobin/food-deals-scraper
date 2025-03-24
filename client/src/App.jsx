import './App.css';
import jsonData from '../../data.json';
import { useState } from 'react';
function App() {
  const [stores, setStores] = useState(jsonData.stores);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mt-3 mb-6 text-gray-800">
        Mina Favoriter! 🎉
      </h1>

      {stores.length > 0 ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {stores.map((store) => (
            <div key={store.id} className="bg-white p-4 rounded-lg shadow-md">
              <h2 className="text-xl font-semibold mt-4">{store.name} </h2>
              <p>{store.address}</p>

              <div className="mt-10 flex flex-col gap-6">
                {store.products.map((product) => (
                  <div
                    key={product.id}
                    className="flex flex-col gap-2 mt-5 mb-5"
                  >
                    <div className="flex justify-center">
                      <img src={product.image} width={150} height={150} />
                    </div>
                    <div className="flex flex-col gap-2 mt-2">
                      <h3 className="font-bold text-slate-800 text-md">
                        {product.title}
                      </h3>
                    </div>
                    <div className="bg-red-100 p-3 rounded-lg flex flex-col gap-2">
                      <p className="text-red-500">
                        Just nu{' '}
                        <span className="font-bold">{product.price}</span>{' '}
                        {store.name.toLocaleLowerCase() === 'willys' ? (
                          <span className="font-bold">kr</span>
                        ) : (
                          ''
                        )}
                      </p>

                      <p>
                        <span>
                          {store.name.toLocaleLowerCase() === 'willys'
                            ? product.save_price
                            : product.original_price}
                        </span>
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      ) : (
        'Inga favoriter just nu.'
      )}
    </div>
  );
}

export default App;
