package com.sml.demo.banking.model;

import java.util.HashMap;

/**
 * Created by kaarthikraaj on 31/10/17.
 */
public class ContextOut{

    private String name;

    private HashMap<String,String> parameters = new HashMap();

    private String lifespan;

    public String getName ()
    {
        return name;
    }

    public void setName (String name)
    {
        this.name = name;
    }

    public HashMap<String, String> getParameters ()
    {
        return parameters;
    }

    public void setParameters (HashMap parameters)
    {
        this.parameters = parameters;
    }

    public String getLifespan ()
    {
        return lifespan;
    }

    public void setLifespan (String lifespan)
    {
        this.lifespan = lifespan;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [name = "+name+", parameters = "+parameters+", lifespan = "+lifespan+"]";
    }
}
