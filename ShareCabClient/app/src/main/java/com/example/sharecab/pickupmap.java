package com.example.sharecab;

import android.content.Intent;
import android.location.Location;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.view.View;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

public class pickupmap extends FragmentActivity implements OnMapReadyCallback,View.OnClickListener,GoogleMap.OnMarkerClickListener {

    private GoogleMap mMap;
    EditText mEdit;
    private Marker myMarker;
    LatLng loc;
    //LatLng sydney = new LatLng(40.0080,-105.258);
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
        Button btn = (Button) findViewById(R.id.button);
        btn.setOnClickListener(this);
        mEdit   = (EditText)findViewById(R.id.loc);
        if(mEdit == null)
        {

        }

    }
    private GoogleMap.OnMyLocationChangeListener myLocationChangeListener = new GoogleMap.OnMyLocationChangeListener() {
        @Override
        public void onMyLocationChange(Location location) {
            loc = new LatLng(location.getLatitude(), location.getLongitude());
            myMarker = mMap.addMarker(new MarkerOptions().position(loc));
            if(mMap != null){
                mMap.animateCamera(CameraUpdateFactory.newLatLngZoom(loc, 16.0f));
            }
        }
    };

    @Override
    public void onClick(View v) {


    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */

    @Override
    public void onMapReady(GoogleMap googleMap) {

        mMap = googleMap;
        mMap.moveCamera(CameraUpdateFactory.newLatLng(loc));
        //mMap.animateCamera(CameraUpdateFactory.zoomTo(10));
        //mMap.addMarker(new MarkerOptions().position(sydney).title("Engineering Center"));
        // Add a marker in Sydney and move the camera
        mMap.addMarker(new MarkerOptions().position(loc).title(""));
        Marker source = mMap.addMarker(new MarkerOptions()
                .position(loc)
                .title(""));
        mMap.setOnMarkerClickListener(this);
        mMap.animateCamera(CameraUpdateFactory.zoomTo(15));


    }

    @Override
    public boolean onMarkerClick(Marker marker) {
        Intent intent = new Intent(this, destinationmap.class);
        startActivity(intent);
        return false;
    }
}
