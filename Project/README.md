# FLASK API 
With CRUD Operations

Hugh O'Reilly
GMIT H.Dip. Data Analytics 
Data Representation Module
___

<table>
<thead>
<tr>
<th>Action</th>
<th>Method</th>
<th>URL</th>
<th>Sample Params</th> 
<th>Sample Return</th>
</tr>
</thead>
<tbody>
<tr>
<td>Get All</td>
<td>GET</td>
<td>/Drug</td>
<td>none</td>
<td>[{...},{...},{...}]</td>  
</tr>
<tr>
<td>Find by id</td>
<td>GET</td>
<td>/Drug/id</td>
<td>none</td>
<td>[{"id":"1","title":"xxx"},{"Manufacturer":"xxx","Revenue($B):"xxx"},{"Disease":"xxx"}]
</td> 
<tr>
<td>Create</td>
<td>POST</td>
<td>/Drug</td>
<td>{"title":"xxx"},{"Manufacturer":"xxx","Revenue($B):"xxx"},{"Disease":"xxx"}</td>
<td>[{"id":"1","title":"xxx"},{"Manufacturer":"xxx","Revenue($B):"xxx"},{"Disease":"xxx"}]
</td>
</tr>
<tr>
<td>Update</td>
<td>PUT</td>
<td>/Drug/id</td>
<td>{"Revenue($B):"xxx"}</td>
<td>[{"id":"1","title":"xxx"},{"Manufacturer":"xxx","Revenue($B):"xxx"},{"Disease":"xxx"}]
</td>
</tr>
<td>Delete</td>
<td>DELETE</td>
<td>/Drug/id</td>
<td>none</td>
<td>{"done:"true}
</td>
</tr>  
</tbody>
</table>

