## Crane comparison (not done in the context of this workshop)
In the context of a different course, I already evaluated some common SfM tools for the reconstruction of Origami paper figures specifically. The goal was to reconstruct the full object as accurately as possible to use as an asset in game production. Therefore, it was important to build a way to capture images of the paper crane from all angles. For this, I used a wire to suspend the paper crane, which can be seen here:

Using this setup, we evaluated three different test scenarios:
1. Static object, camera moves around it.
2. Static camera, object was moved to capture it from all angles.
3. Static object, camera moves around it with a textured surface below the wire holding the crane.

Versions 1 and 2 resulted in parts of my room being reconstructed, but no crane as can be seen here:

<table>
    <thead>
        <tr>
            <th>RealityCapture</th>
            <th>Colmap</th>
            <th>Meshroom</th>
            <th>Polycam</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>v1</th>
            <td>~30 minutes</td>
            <td>~2.5 hours</td>
            <td>not tested</td>
        </tr>
    </tbody>
</table>

<table>
  <thead>
    <tr>
      <th>Tools</th>
      <th>Result</th>
      <th>side</th>
      <th>front</th>
      <th>45°</th>
      <th>No. of points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Colmap<br><small>2016</small></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0</td>
    </tr>
    <tr>
      <td>Polycam<br><small>2020</small></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0</td>
    </tr>
    <tr>
      <td>Meshroom<br><small>9 August 2018</small></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0</td>
    </tr>
    <tr>
      <td>Dust3r<br><small>21 Dec 2023</small></td>
    </tr>
    <tr>
      <td>Mast3r<br><small>14 Jun 2024</small></td>
    </tr>
    <tr>
      <td>Spann3r<br><small>28 Aug 2024</small></td>
    </tr>
    <tr>
      <td>VGGT<br><small>14 Mar 2025</small></td>
    </tr>
  </tbody>
</table>