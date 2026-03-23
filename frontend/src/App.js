
import axios from "axios";
function App(){
 const upload=async(e)=>{
  const f=e.target.files[0];
  const fd=new FormData(); fd.append("file",f);
  const res=await axios.post("http://localhost:8000/layout/",fd);
  console.log(res.data);
 }
 return(
  <div>
   <h2>Solar Tool</h2>
   <input type="file" onChange={upload}/>
  </div>
 );
}
export default App;
