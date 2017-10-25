package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */

public class Inputs
{
    private Raw_inputs[] raw_inputs;

    private Arguments[] arguments;

    private String intent;

    public Raw_inputs[] getRaw_inputs ()
    {
        return raw_inputs;
    }

    public void setRaw_inputs (Raw_inputs[] raw_inputs)
    {
        this.raw_inputs = raw_inputs;
    }

    public Arguments[] getArguments ()
    {
        return arguments;
    }

    public void setArguments (Arguments[] arguments)
    {
        this.arguments = arguments;
    }

    public String getIntent ()
    {
        return intent;
    }

    public void setIntent (String intent)
    {
        this.intent = intent;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [raw_inputs = "+raw_inputs+", arguments = "+arguments+", intent = "+intent+"]";
    }
}

