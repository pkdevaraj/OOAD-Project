package com.example.sharecab;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.*;
import java.lang.*;
import android.app.Activity;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
public class driverHome extends Activity implements AdapterView.OnItemClickListener {
    // Array of strings...
    Date date = new Date();
    DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
    String[] mobileArray = {"MY BOOKINGS", "2016/04/24 20:04:00","2016/04/26 02:02:00",dateFormat.format(date).toString()};
    ListView listView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //Toast.makeText(this, "Booking Successful", Toast.LENGTH_SHORT).show();
        Date date = new Date();
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        setContentView(R.layout.activity_home);
        ArrayAdapter adapter = new ArrayAdapter<String>(this, R.layout.support_simple_spinner_dropdown_item, mobileArray);


        listView = (ListView) findViewById(R.id.mobile_list);
        listView.setAdapter(adapter);
        if (mobileArray == null || mobileArray.length == 0) {
            Toast.makeText(this, "", Toast.LENGTH_SHORT).show();

        }
        listView.setOnItemClickListener(this);
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        Toast.makeText(getApplicationContext(), "New Booking", Toast.LENGTH_SHORT).show();
        listView.setVisibility(View.INVISIBLE);
        Intent intent = new Intent(
                getApplicationContext(), driverdropoff.class);
        startActivity(intent);
    }



    }