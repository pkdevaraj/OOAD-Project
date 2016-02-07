package com.example.cabsharing;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;

public class ConfirmDetails extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_confirm_details);
		onClickButton();
		Spinner shareCountDropdown = (Spinner)findViewById(R.id.spinner2);
		Spinner passengerDropdown = (Spinner)findViewById(R.id.spinner1);
		String[] passengerCount = new String[]{"1", "2", "3"};
		ArrayAdapter<String> passengeradapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_dropdown_item, passengerCount);
		passengerDropdown.setAdapter(passengeradapter);
		
		String[] shareNumber = new String[]{"1", "2", "3"};
		ArrayAdapter<String> Countadapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_dropdown_item, shareNumber);
		shareCountDropdown.setAdapter(Countadapter);
	}

	public void onClickButton() {
		Button b1 = (Button) findViewById(R.id.button1);
		Button b2 = (Button) findViewById(R.id.button2);
        b1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				  Log.i("clicks"," Book Clicked");
				  startActivity(new Intent(ConfirmDetails.this, Summary.class));
			}
		});	
        b2.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				  Log.i("clicks","Logout Clicked");
				  startActivity(new Intent(ConfirmDetails.this, MainActivity.class));
			}
		});	
	}
	

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		// Handle action bar item clicks here. The action bar will
		// automatically handle clicks on the Home/Up button, so long
		// as you specify a parent activity in AndroidManifest.xml.
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			return true;
		}
		return super.onOptionsItemSelected(item);
	}
}
