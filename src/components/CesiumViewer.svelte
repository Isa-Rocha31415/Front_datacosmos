<script lang="ts">
  import { onMount } from 'svelte';
 import * as Cesium from 'cesium';
import 'cesium/Build/Cesium/Widgets/widgets.css';
Cesium.buildModuleUrl.setBaseUrl('/Cesium/');

  let viewer;

  onMount(async () => {
   
Cesium.Ellipsoid.default = Cesium.Ellipsoid.MOON;
    const moonRadius = 1737400;
    const moonEllipsoid = Cesium.Ellipsoid.fromCartesian3(
      new Cesium.Cartesian3(moonRadius, moonRadius, moonRadius)
    );


    viewer = new Cesium.Viewer('cesiumContainer', {
      sceneMode: Cesium.SceneMode.SCENE3D,
      globe: new Cesium.Globe(moonEllipsoid),
      imageryProvider: undefined,   // <-- disable default Earth imagery
      baseLayerPicker: false,
      terrainProvider: new Cesium.EllipsoidTerrainProvider({ ellipsoid: moonEllipsoid }),
      geocoder: false,
      sceneModePicker: false,
         
    });

   const tileset = await Cesium.Cesium3DTileset.fromIonAssetId(2684829);
    viewer.scene.primitives.add(tileset);

    const northPoleRect = [
      Cesium.Rectangle.fromDegrees(-180, 60, -90, 90),
      Cesium.Rectangle.fromDegrees(-90, 60, 0, 90),
      Cesium.Rectangle.fromDegrees(0, 60, 90, 90),
      Cesium.Rectangle.fromDegrees(90, 60, 180, 90),
      Cesium.Rectangle.fromDegrees(-180, 30, -90, 60),
      Cesium.Rectangle.fromDegrees(-90, 30, 0, 60),
      Cesium.Rectangle.fromDegrees(0, 30, 90, 60),
      Cesium.Rectangle.fromDegrees(90, 30, 180, 60),
    ];

    const southPoleRectangles = [
      Cesium.Rectangle.fromDegrees(-180, -90, -135, -60),
      Cesium.Rectangle.fromDegrees(-135, -90, -90, -60),
      Cesium.Rectangle.fromDegrees(-90, -90, 0, -60),
      Cesium.Rectangle.fromDegrees(-45, -90, 0, -60),
      Cesium.Rectangle.fromDegrees(0, -90, 45, -60),
      Cesium.Rectangle.fromDegrees(135, -90, 180, -60),
    ];

    const equatorialRectangles = [];
    for (let i = 0; i < 35; i++) {
      equatorialRectangles.push(Cesium.Rectangle.fromDegrees(
        -180 + i * (360 / 35), 0,
        180 - (i + 1) * (360 / 35), 30
      ));
    }

    const allRectangles = [
      ...northPoleRect,
      ...equatorialRectangles,
      ...southPoleRectangles
    ];

    for (let i = 0; i < allRectangles.length; i++) {
      const moonTiles = new Cesium.UrlTemplateImageryProvider({
        url: `http://127.0.0.1:8000/out1/moon_polar_tiles${i + 1}/{z}/{x}/{y}.png`,
        tilingScheme: new Cesium.GeographicTilingScheme(),
        rectangle: allRectangles[i],
        maximumLevel: 8
      });
     // moonTiles.tileDiscardPolicy = new Cesium.DiscardEmptyTileImagePolicy();
      viewer.imageryLayers.addImageryProvider(moonTiles);
    }

    viewer.camera.flyTo({
      destination: Cesium.Cartesian3.fromDegrees(180, 0, moonRadius * 3),
      orientation: {
        heading: Cesium.Math.toRadians(180),
        pitch: Cesium.Math.toRadians(-90),
        roll: 0
      }
    });
  });
</script>

<style>
  #cesiumContainer {
    width: 100%;
    height: 100vh;
   
  }
</style>

<div id="cesiumContainer"></div>
