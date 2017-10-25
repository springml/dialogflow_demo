package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 23/10/17.
 */



public class Raw_inputs
{
    private String query;

    private String input_type;

    public String getQuery ()
    {
        return query;
    }

    public void setQuery (String query)
    {
        this.query = query;
    }

    public String getInput_type ()
    {
        return input_type;
    }

    public void setInput_type (String input_type)
    {
        this.input_type = input_type;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [query = "+query+", input_type = "+input_type+"]";
    }
}

