package com.sml.demo.banking.model;

/**
 * Created by kaarthikraaj on 24/10/17.
 */
public class Contexts
{
    private String name;

    private Parameters parameters;

    private String lifespan;

    public String getName ()
    {
        return name;
    }

    public void setName (String name)
    {
        this.name = name;
    }

    public Parameters getParameters ()
    {
        return parameters;
    }

    public void setParameters (Parameters parameters)
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
