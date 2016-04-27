package com.example.sharecab;

import android.content.Intent;
import android.location.Location;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import static java.lang.Thread.sleep;

public class drivermap extends FragmentActivity implements OnMapReadyCallback, View.OnClickListener {
    LatLng loc;
    private GoogleMap mMap;
    Button btn,refreshbtn;
    private Marker myMarker;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_drivermap);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
        refreshbtn = (Button) findViewById(R.id.button4);
        btn = (Button) findViewById(R.id.button);
        btn.setVisibility(View.INVISIBLE);
        //Button btn = (Button) findViewById(R.id.button);
        refreshbtn.setOnClickListener(this);
        btn.setOnClickListener(this);
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
    public void onClick(View v) {
        //mMap.addMarker(new MarkerOptions().position(sydney).title("Denver Airport"));
        switch (v.getId()) {
            case R.id.button:
                Intent intent = new Intent(this, driverdropoff.class);
                startActivity(intent);
            case R.id.button4:

                break;
        }
        }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        mMap.moveCamera(CameraUpdateFactory.newLatLng(loc));
        btn.setVisibility(View.VISIBLE);
        mMap.addMarker(new MarkerOptions().position(loc).title(""));
        mMap.animateCamera(CameraUpdateFactory.zoomTo(15));
        // Add a marker in Sydney and move the camera

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
}
