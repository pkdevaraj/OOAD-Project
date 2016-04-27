package com.example.sharecab;

import android.app.ListActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.*;
import java.lang.*;
import android.app.Activity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.os.Bundle;
import android.app.Activity;
import android.view.Gravity;
import android.view.View;
import android.view.ViewGroup.LayoutParams;
import android.widget.*;
import android.view.LayoutInflater;
import android.view.Menu;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import java.util.Date;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
public class home extends Activity implements AdapterView.OnItemClickListener {
    // Array of strings...
    Date date = new Date();
    DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
    String[] mobileArray = {"MY BOOKINGS",dateFormat.format(date).toString()};
    ListView listView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Toast.makeText(this, "Booking Successful", Toast.LENGTH_SHORT).show();
        Date date = new Date();
        DateFormat dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
        setContentView(R.layout.activity_home);
        //String[] mobileArray = {dateFormat.format(date).toString()};
        ArrayAdapter adapter = new ArrayAdapter<String>(this, R.layout.support_simple_spinner_dropdown_item, mobileArray);


        listView = (ListView) findViewById(R.id.mobile_list);
        listView.setAdapter(adapter);
        if (mobileArray == null || mobileArray.length == 0) {
            Toast.makeText(this, "The list is empty", Toast.LENGTH_SHORT).show();

        }
        listView.setOnItemClickListener(this);
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
        LayoutInflater layoutInflater
                = (LayoutInflater) getBaseContext()
                .getSystemService(LAYOUT_INFLATER_SERVICE);
        View popupView = layoutInflater.inflate(R.layout.popup, null);
        final PopupWindow popupWindow = new PopupWindow(
                popupView,
                LayoutParams.WRAP_CONTENT,
                LayoutParams.WRAP_CONTENT);

        Button btnDismiss = (Button) popupView.findViewById(R.id.ok);
        btnDismiss.setOnClickListener(new Button.OnClickListener() {

            @Override
            public void onClick(View v) {
                //TODO Auto-generated method stub

                popupWindow.dismiss();
                Toast.makeText(getApplicationContext(), "Booking Cancelled", Toast.LENGTH_SHORT).show();
                listView.setVisibility(View.INVISIBLE);
                Intent intent = new Intent(
                        getApplicationContext(), pickupmap.class);
                startActivity(intent);

            }
        });

        popupWindow.showAtLocation(popupView, Gravity.CENTER, 0, 0);

    }
}